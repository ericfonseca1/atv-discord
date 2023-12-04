#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void comunidades();
void trello();
void discord();
void mentoria();
void empregabilidade();
void github();
void softskills();
void noticias_tech();

typedef struct{
	int codigo;
	int n_turma;
	int n_matricula;
	char nome[30];
}solicite;

int main() {
	
	setlocale(LC_ALL,"Portuguese");
	
	printf("\n\t-------------------");
	printf("\n\tSistema Comunidades\n");
	printf("\t-------------------");
	comunidades();
	
	return 0;
}

void comunidades(){
	
	solicite escolha;
	
	do{
    	printf("\n\n\t\t|MENU|\n");
   		printf("\n 1- Comunidade Trello\n");
   		printf(" 2- Comunidade Discord\n");
    	printf(" 3- Comunidade Mentoria\n");
    	printf(" 4- Comunidade Empregabilidade\n");
    	printf(" 5- Comunidade Github\n");
    	printf(" 6- Comunidade Softskills\n");
    	printf(" 7- Comunidade Noticias Tech\n");
    	printf(" 8- Sair do Sistema\n");
        printf("\n Digite o codigo do setor: ");
   		scanf("%i",&escolha.codigo);
       
     switch(escolha.codigo){  
	        case 1:
	        	trello();
	        break;
	        
	        case 2: 
	        	discord();
	        break;
	        
	        case 3:
	        	mentoria();
	        break;
	        
	        case 4: 
	        	empregabilidade();
	        break;
	        
	        case 5: 
	        	github();
	        break;
	        
	        case 6:
	        	softskills();
	        break;
	        
	        case 7:
	        	noticias_tech();
	        break;
	        
	        case 8:
	        	printf("\n Saindo do Sistema...");
	        break;
	        
	        default:
	        	printf(" CODIGO INVALIDO!");
	        	printf(" Por favor, digite um codigo de 1 a 8\n");
			
		}
	}while(escolha.codigo != 8);
}

void trello(){
}
void discord(){
}
void mentoria(){
}
void empregabilidade(){
}
void github(){
}
void softskills(){
}
void noticias_tech(){
}

