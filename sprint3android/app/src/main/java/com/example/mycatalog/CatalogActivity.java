package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {

    private Button button; //Añadimos el atributo privado de Button
    private Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);

        button = findViewById(R.id.buttonAC); //Asociamos el Botton con el ID
        button.setOnClickListener(new View.OnClickListener() { //Le asociamos una acción para cuando hagamos click en el botón
            @Override
            public void onClick(View view) {
                //Iniciamos una nueva Actividad cada vez que se pulse en el botón
                Intent intent = new Intent(context, DetailActivity.class);
                context.startActivity(intent);
            }
        });
    }
}