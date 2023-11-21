package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class F1Data {

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

}
