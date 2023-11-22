package com.example.myothercatalog;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) { //Creamos la interfaz de usuario...
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail); //Para ello inflamos el diseño de la actividad con su xml correspondiente
    }
}
