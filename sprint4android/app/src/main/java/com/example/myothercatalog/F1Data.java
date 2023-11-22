package com.example.myothercatalog;

import android.os.Parcel;
import android.os.Parcelable;

import androidx.annotation.NonNull;

import org.json.JSONException;
import org.json.JSONObject;

public class F1Data implements Parcelable {

    //Elementos que componen el JSON del github
    private String name;
    private String description;
    private String image_url;

    //Creación del constructor que recuperará los elementos del JSON
    public F1Data(JSONObject json) {
        try {
            this.name = json.getString("name");
            this.description = json.getString("description");
            this.image_url = json.getString("image_url");
        }catch(JSONException e) {
            e.printStackTrace();}
    }

    //Getters y setters
    public String getImage_url() {
        return image_url;
    }

    public void setImage_url(String image_url) {
        this.image_url = image_url;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


    //Constructor "Protegido" al que se le pasa como parámetro Parcelable
    protected F1Data(Parcel in) {
        // Lee las cadenas Parcel, así como las asigna a campos según su correspondencia
        name = in.readString();
        description = in.readString();
        image_url = in.readString();
    }

    // Implementación de la Interfaz Parcelable
    public static final Creator<F1Data> CREATOR = new Creator<F1Data>() {
        // Método que crea una instancia de F1data
        @Override
        public F1Data createFromParcel(Parcel in) {
            return new F1Data(in);
        }
        // Método que crea un array de F1Data con el tamaño especifico
        @Override
        public F1Data[] newArray(int size) {
            return new F1Data[size];
        }

    };
    // Método que describe los tipos de objetos contenidos en el Parcelable
    @Override
    public int describeContents() {
        return 0;
    }
    // Método que escribe los valores de los campos de la clase en un Parcel
    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(name);
        dest.writeString(description);
        dest.writeString(image_url);
    }
}
