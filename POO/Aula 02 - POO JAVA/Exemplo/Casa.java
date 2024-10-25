package Exemplo;

import java.util.ArrayList;
import java.util.List;

public class Casa {
    private String endereco;
    private List<Gato> gatos;

    public String getEndereco() {
        return this.endereco;
    }
    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
    public List<Gato> getGatos() {
        return this.gatos;
    }
    public void setGatos(List<Gato> gatos) {
        this.gatos = gatos;
    }

    public void Casa(String endereco){
        this.gatos = new ArrayList<>();
        this.endereco = endereco;
    }
    public void adotarGato(Gato gato){
        gatos.add(gato);
    }
    public void chamarMoradores(){
        for (Gato gato: this.gatos){
            System.out.printf("%s \n",gato.getNome());
        }
    }

    
}
