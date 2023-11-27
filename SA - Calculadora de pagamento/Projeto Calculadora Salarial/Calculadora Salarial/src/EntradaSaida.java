import javax.swing.JOptionPane;

public class EntradaSaida {

    public static int menuLogin(int opcao) {
        return Integer.parseInt(JOptionPane.showInputDialog("MENU\n[1]-Entrar como usuario\n[2]-Acessar painel de administrador\n[3]-Cadastrar novo usuario"));
    }
    
}
