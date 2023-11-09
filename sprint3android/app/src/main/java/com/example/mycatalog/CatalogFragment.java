package com.example.mycatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

public class CatalogFragment extends Fragment { //Indicamos que es un fragmento con el extends Fragment

    private Button button; //Añadimos el atributo privado de Button
    private Context context;

    public static CatalogFragment newInstance(@StringRes int textId) { //Instanciamos el fragmento el cual recibirá el parámetro textId para ser identificado
        CatalogFragment fr = new CatalogFragment();
        return fr;
    }

    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable //Creamos la interfaz de usuario. Para ello...
    Bundle savedInstanceState) {
        View layout = inflater.inflate(R.layout.catalog_fragment, container, false); //Inflamos el fragmento con el xml
        button = layout.findViewById(R.id.buttonCF); //Asociamos un botón con el id
        button.setOnClickListener(new View.OnClickListener() { //El cual estará atento si pulsamos en el o no
            @Override
            public void onClick(View view) { //Si pulsamos en el. Actuará onClick...
                // Iniciando la DetailActivity con intent y startActivity.
                Intent intentDetailActivity = new Intent(context, DetailActivity.class);
                startActivity(intentDetailActivity);
            }
        });
        return layout;
    }
    // Este método guarda el context del Fragment:
    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        this.context = context;
    }

}
