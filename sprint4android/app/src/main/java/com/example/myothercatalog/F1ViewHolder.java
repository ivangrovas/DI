package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class F1ViewHolder extends RecyclerView.ViewHolder {

    //Elementos de la interfaz de usuario que muestra los datos
    private final TextView textView;
    private  final ImageView imageView;
    // Constructor que recibe la vista que representa un elemento individual del RecyclerView
    public F1ViewHolder (@NonNull View itemView){
        super(itemView);
        // Inicialización los elementos de la UI mediante sus ids
        textView = (TextView) itemView.findViewById(R.id.f1_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.f1_image_view);
    }
    // Método que muestra datos en los elementos de la UI
    public  void showData(F1Data data, Activity activity){
        //Recuperamos el elemento nombre de los datos para añadirlo al texto del TextView
        textView.setText(data.getName());
        //La biblioteca Glide, la cual cargar y muestra la imagen desde la URL proporcionada
        Glide.with(itemView.getContext()).load(data.getImage_url()).into(imageView);
    }
}
