package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.ListAdapter;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class F1RecyclerViewAdapter extends RecyclerView.Adapter<F1ViewHolder> {
    //Lista de datos de f1 que se mostrarán en el recyclerView
    private List<F1Data> allTheData;
    // Referencia a la actividad que contiene el RecyclerView
    private Activity activity;
    //Constructor que recibe los datos
    public F1RecyclerViewAdapter(List<F1Data> dataSet, Activity activity){
        this.allTheData = dataSet;
        this.activity = activity;
    }
    // Método para crear un nuevo ViewHolder
    @NonNull
    @Override
    public F1ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.f1_view_holder,parent,false);
        // Devolución de un ViewHolder asociado a la vista inflada
        return new F1ViewHolder(view);
    }
    // LLamada para mostrar datos en una posición específica del RecyclerView
    @Override
    public void onBindViewHolder(@NonNull F1ViewHolder holder, int position) {
        F1Data dataInPositionToBeRendered = allTheData.get(position);

        // Llamada al método showData() con el bojetivo de mostrar los datos
        holder.showData(dataInPositionToBeRendered, activity);
    }
    //Método que devuelve el número total de elementos en el conjuto de datos
    @Override
    public int getItemCount() {
        return allTheData.size();
    }
}
