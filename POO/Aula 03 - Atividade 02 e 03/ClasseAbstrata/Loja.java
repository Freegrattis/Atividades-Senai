public abstract class Loja {
    private static int contador = 0;
    private int identificador;
    private String cnpj;
    protected String razaoSocial;
    protected boolean aberta;

    // Construtor
    public Loja(String cnpj, String razaoSocial) {
        this.identificador = ++contador;
        this.cnpj = cnpj;
        this.razaoSocial = razaoSocial;
        this.aberta = false;
    }

    // Método
    public String getDados() {
        String status = aberta ? "Aberta" : "Fechada";
        return "Razão Social: " + razaoSocial + ", CNPJ: " + cnpj + ", Status: " + status;
    }
}
