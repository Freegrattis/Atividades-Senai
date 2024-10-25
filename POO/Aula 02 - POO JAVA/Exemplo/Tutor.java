package Exemplo;

import java.util.ArrayList;
import java.util.List;

public class Tutor {
    private String nome;
    private List<ArrayList> gatos;

    public String getNome() {
        return this.nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public List<ArrayList> getGatos() {
        return this.gatos;
    }
    public void setGatos(List<ArrayList> gatos) {
        this.gatos = gatos;
    }

    public Tutor(String nome, Gato gato){
        this.nome = nome;
        this.gatos = new ArrayList<>();
        this.gatos.add(null);
    }

    public void inserirGato(Gato gato){
        this.gatos.add(gato);
    }

    public void chamarGato(String nomeGato) {
        I
        for (Gato gato : gatos) {
            if (gato.getNome().equals(nomeGato)) {
                System.out.println("Vem aqui, " + gato.getNome() + "!");
                return;
            }
        }
        System.out.println(nomeGato + " não foi encontrado.");
    }

    
}
