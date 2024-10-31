public class LojaShopping extends Loja implements Registro {
    private String endereco;
    private String gerente;

    public LojaShopping(String cnpj, String razaoSocial, String endereco, String gerente) {
        super(cnpj, razaoSocial);
        this.endereco = endereco;
        this.gerente = gerente;
    }

    @Override
    public void registraAberturaDia() {
        if (!aberta) {
            aberta = true;
            System.out.println("Loja " + razaoSocial + " aberta.");
        } else {
            System.out.println("A loja " + razaoSocial + " já está aberta.");
        }
    }

    @Override
    public void registraFechamentoDia() {
        if (aberta) {
            aberta = false;
            System.out.println("Loja " + razaoSocial + " fechada.");
        } else {
            System.out.println("A loja " + razaoSocial + " já está fechada.");
        }
    }

    // Método para mostrar todos os dados da loja
    public String mostrarDados() {
        return getDados() + ", Endereço: " + endereco + ", Gerente: " + gerente;
    }
}
