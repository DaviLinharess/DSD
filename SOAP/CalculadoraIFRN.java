import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.xml.ws.Endpoint;

@WebService(targetNamespace = "http://ifrn.edu.br/")
public class CalculadoraIFRN {

    // Calcula a média parcial ponderada dos bimestres (2 para o 1º e 3 para o 2º)
    @WebMethod
    public double calcularMediaParcial(
            @WebParam(name = "nota1Bimestre") double n1, 
            @WebParam(name = "nota2Bimestre") double n2) throws Exception {
        
        // Validação básica de erro 
        if (n1 < 0 || n1 > 100 || n2 < 0 || n2 > 100) {
            throw new Exception("As notas dos bimestres devem estar entre 0 e 100.");
        }
        
        return ((n1 * 2) + (n2 * 3)) / 5.0;
    }
 
    // Situação do aluno com base na média e na nota da PF
    @WebMethod
    public String verificarSituacao(
            @WebParam(name = "mediaParcial") double mediaParcial, 
            @WebParam(name = "notaProvaFinal") double notaPF) throws Exception {
        
        if (mediaParcial < 0 || mediaParcial > 100 || notaPF < 0 || notaPF > 100) {
            throw new Exception("Valores inválidos. As notas devem estar entre 0 e 100.");
        }

        // Aprovado Direto
        if (mediaParcial >= 60.0) {
            return "Aprovado por Média";
        } 
        // Reprovado Direto (Abaixo de 20 nem vai para a Prova Final)
        else if (mediaParcial < 20.0) {
            return "Reprovado Direto";
        } 
        // Apto à Prova Final (Entre 20 e 60)
        else {
            // Se a notaPF for 0, significa que ele ainda não fez a prova
            if (notaPF == 0) {
                return "Apto a fazer a Prova Final";
            }
            
            // Se ele fez a prova final, faz o cálculo
            double mediaFinal = (mediaParcial + notaPF) / 2.0;
            if (mediaFinal >= 60.0) {
                return "Aprovado na Prova Final (Média Final: " + mediaFinal + ")";
            } else {
                return "Reprovado na Prova Final (Média Final: " + mediaFinal + ")";
            }
        }
    }

    public static void main(String[] args) {
        String url = "http://localhost:8080/ws/calculadora";
        System.out.println("Servidor SOAP Ativo");
        System.out.println("Contrato WSDL gerado em: " + url + "?wsdl");
        Endpoint.publish(url, new CalculadoraIFRN());
    }
}