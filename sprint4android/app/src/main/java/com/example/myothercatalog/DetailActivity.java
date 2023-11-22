package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) { //Creamos la interfaz de usuario...
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail); //Para ello inflamos el diseño de la actividad con su xml correspondiente
        // Referencias a los elementos de la interfaz de usuario en activity_detail.xml

        // Obtención de la información del intent
        F1Data f1data = getIntent().getParcelableExtra("f1data");

        ImageView imageView = findViewById(R.id.ImageViewAC);
        TextView textTitle = findViewById(R.id.textViewTitleAC);
        TextView textDescription = findViewById(R.id.textDescription);

        // Mostrar la información de la UI
        textTitle.setText(f1data.getName());
        textDescription.setText(f1data.getDescription());

        // Utilizar Glide para cargar la imagen desde la URL y mostrarla en el ImageView
        Glide.with(this)
                .load(f1data.getImage_url())
                .into(imageView);
    }
}
