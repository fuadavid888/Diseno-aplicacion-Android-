package com.example.vetlink;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CalendarView;
import android.widget.Toast;
import androidx.fragment.app.Fragment;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link SecondFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class SecondFragment extends Fragment {

    // Parameters for the fragment
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";
    private String mParam1;
    private String mParam2;

    public SecondFragment() {
        // Required empty public constructor
    }

    public static SecondFragment newInstance(String param1, String param2) {
        SecondFragment fragment = new SecondFragment();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_second, container, false);

        // Vincula el CalendarView desde el layout
        CalendarView calendarView = view.findViewById(R.id.calendarView);

        // Establece el listener para la selección de la fecha
        calendarView.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {
            @Override
            public void onSelectedDayChange(CalendarView view, int year, int month, int dayOfMonth) {
                // Formatea la fecha seleccionada
                String selectedDate = dayOfMonth + "/" + (month + 1) + "/" + year;

                // Muestra un Toast con la fecha seleccionada (puedes guardar esta fecha en una base de datos o en preferencia)
                Toast.makeText(getActivity(), "Fecha seleccionada: " + selectedDate, Toast.LENGTH_SHORT).show();

                // Aquí puedes agregar lógica adicional para agendar una cita
                // Por ejemplo, guardar la fecha en una base de datos o en SharedPreferences
            }
        });

        return view;
    }
}
