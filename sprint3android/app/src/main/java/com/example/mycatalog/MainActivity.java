package com.example.mycatalog;

import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;

import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;

import androidx.appcompat.widget.Toolbar;
import androidx.fragment.app.Fragment;

import com.google.android.material.navigation.NavigationView;

public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {
    private DrawerLayout drawerLayout;
    private MenuItem catalogItem;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Configuración Tolbar
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        //Configuración del DrawerLayout
        drawerLayout = findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);

        toggle.syncState();

        //Configuración NavigationView
        NavigationView navigationView = findViewById(R.id.nav_View);
        navigationView.setNavigationItemSelectedListener(this);

        //Obtención del encabezado de la NavigationView
        View header = navigationView.getHeaderView(0);
        header.findViewById(R.id.header_title);
    }

    //Función que muestra el fragmento del elemento que seleccione el usuario
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
        showFragment(getTitle(menuItem));
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }
    //Código para que al pulsar el botón atrás del móvil se cierre el menú del navigation drawer:
    @Override
    public void onBackPressed() {

        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }
    //Método que enviará el respectivo id del elemento que seleccione el usuario al onNavigationItemSelected
    private int getTitle(@NonNull MenuItem menuItem) {
        String nombre = String.valueOf(menuItem.getTitle());
        switch (nombre) {
            case "Catalog":
                return R.string.menu_catalog;
            case "About":
                return R.string.menu_about;
            default:
                throw new IllegalArgumentException("pending for developer");
        }
    }
    //Función para que según el id que el usuario selecciona (elemento que pulsa) muestre el respectivo título del fragmento en la parte superior de la actividad.
    private void showFragment(@StringRes int titleId) {
        if (titleId == R.string.menu_catalog) {
            Fragment fragment = CatalogFragment.newInstance(titleId);
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, fragment).commit();
            setTitle(getString(titleId));

        } else if (titleId == R.string.menu_about) {
            Fragment fragment = AboutFragment.newInstance(titleId);
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, fragment).commit();
            setTitle(getString(titleId));
        }
    }
}

