package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.ListAdapter;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class F1RecyclerViewAdapter extends RecyclerView.Adapter<F1ViewHolder> {
    //Lista de datos de f1 que se mostrarán en el recyclerView
    private List<F1Data> allTheF1;
    // Referencia a la actividad que contiene el RecyclerView
    private Activity activity;

    private OnItemClickListener mListener;

    public interface OnItemClickListener{
        void onItemClick(int position); //Método al que se llama al hacer clic en la celda, se le manda la posición
    }
    // Método para establecer el OnItemClickListener en la clase
    public void setOnItemClickListener(OnItemClickListener listener){
        mListener=listener;
    }
    //Constructor que recibe los datos
    public F1RecyclerViewAdapter(List<F1Data> dataSet, Activity activity){
        this.allTheF1 = dataSet;
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
        F1Data dataInPositionToBeRendered = allTheF1.get(position);

        // Llamada al método showData() con el bojetivo de mostrar los datos
        holder.showData(dataInPositionToBeRendered, activity);
        final int adapterPosition = holder.getAdapterPosition();
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) { // Se ejecuta cuando se hace clic en el elemento de la vista del ViewHolder
                if (mListener != null && adapterPosition != RecyclerView.NO_POSITION) {
                    mListener.onItemClick(adapterPosition);
                    // Verificamos si mListener es/no es nulo y si
                    // la posición de adapterPosition es válido en el RecyclerView
                }
            }
        });
    }
    //Método que devuelve el número total de elementos en el conjuto de datos
    @Override
    public int getItemCount() {
        return allTheF1.size();
    }
}
