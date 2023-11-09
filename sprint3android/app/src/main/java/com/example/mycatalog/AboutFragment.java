package com.example.mycatalog;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

public class AboutFragment extends Fragment { //Indicamos que es un fragmento con el extends Fragment
    public static AboutFragment newInstance(@StringRes int textId) { //Instanciamos el fragmento el cual recibirá el parámetro textId para ser identificado
        AboutFragment fm = new AboutFragment();
        return fm;
    }
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable //Creamos la interfaz de usuario. Para ello...
    Bundle savedInstanceState) {
        View layout = inflater.inflate(R.layout.about_fragment, container, false); //Inflamos el fragmento con el xml

        return layout;
    }
}
