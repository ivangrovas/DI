package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.ListAdapter;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicialización del RecyclerView
        RecyclerView recyclerView = findViewById(R.id.recyclerView);

        // Actividad actual referenciada
        Activity activity = this;

        // Creación de la solicitud JSON para obtener datos de la URL proporcionada
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/ivangrovas/DI/main/recursos/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Almacén de los datos del JSON de F1
                        List<F1Data> allTheF1 = new ArrayList<>();

                        // Iteración del JSON Array para extraer y procesar datos
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                // Obtención de un objeto JSON que representa un dato de F1
                                JSONObject f1 = response.getJSONObject(i);

                                // Cración del objeto F1Data a partir del JSON obtenido previamente
                                F1Data data = new F1Data(f1);

                                // Agregación del objeto F1Data a la lista
                                allTheF1.add(data);
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }

                        // Creación y configuración del adaptador del RecyclerView
                        F1RecyclerViewAdapter adapter = new F1RecyclerViewAdapter(allTheF1, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                        adapter.setOnItemClickListener(new F1RecyclerViewAdapter.OnItemClickListener() {
                            @Override
                            public void onItemClick(int position) {
                                F1Data clickedCoche = allTheF1.get(position);
                                Intent intent = new Intent(MainActivity.this, DetailActivity.class);
                                intent.putExtra("f1data", clickedCoche); //Pasamos los datos a la nueva actividad
                                startActivity(intent);
                            }
                        });
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Respuesta en caso de error
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });

        // Obtención de la cola de solicitudes Volley
        RequestQueue cola = Volley.newRequestQueue(this);
        //Agregación de la solicitud
        cola.add(request);
    }
}