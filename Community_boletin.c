#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <stdlib.h>
#include <conio.h>

void meni1();
void meni2();
void empregabilidade();
void noticias_tech();
void trello();
void github();
void monitoria();
void lideres();
void softskills();
void discord();
void boletim();

int cont;
typedef struct{
	char nome[50];
	char comunidade[30];
}alunos;

alunos alun[26] = {{"Albert Duarte Costa","Discord"},{"Altair de Jesus Santos Junior", "Trello"},{"Amanda Oliveira da Silva","Softskills"},
{"Ana Caroline da Silva Muniz","Empregabilidade"},{"Antonio de Sousa Silva","Empregabilidade"},
{"Átila Conceição de Goes","Lideres"},{"Caique Vidal Gonzaga de Freitas","Monitoria"},
{"Douglas Henrique da Conceição Souza","Notícias Tech"},{"Eduardo Santos da Conceicão","Trello"},
{"Eric dos Santos Fonseca","Discord"},{"Erick Macedo de Almeida","Github"},{"Filipe Da Silva Santos","Monitoria"},
{"Filipe Sobreira Campos","Notícias Tech"},{"Gabriele de Jesus da Costa","Monitoria"},{"Liliana Lima do Carmo","Empregabilidade"},
{"Luiz Claudio Meneses dos Santos","Discord"},{"Marlon Gabriel Araujo dos Santos","Monitoria"},
{"Marta São Pedro de Santana Cordolino","Trello"},{"Mateus Ferreira de Oliveira","Notícias Tech"},
{"Matheus Santa Rita dos Santos","Lideres"},{"Pedro César Da Silva Santos Júnior","Github"},
{"Ramon Fernando Miranda de Oliveira","Empregabilidade"},{"Sédriky Logan Dantas de Oliveira","Softskills"},
{"Tamires dos Santos de Jesus","Softskills"},{"Tawan Correia Leonel","Empregabilidade"},{"Thalys Márcio Bezerra Neves","Monitoria"}};

int main(){
	setlocale(LC_ALL,"Portuguese");
	meni1();	
	return 0;
}


void meni1(){
	
	int menu1;

	do{
		printf("\n =============================\n");
		printf("\t DISCORD");
		printf("\n =============================\n\n");
		printf(" 1 - Acessar Link\n");
		printf(" 2 - Acessar Comunidades\n");
		printf(" 3 - Acessar Boletim\n");
		printf(" 4 - Sair do sistema\n");
		printf(" Escolha uma opção do menu: ");
		scanf("%d", &menu1);
		system("cls");
		
		//Opções do primeiro menu (Link,Comunidades, Boletim)
		switch (menu1){
			case 1:
				puts("\n Link para acessar o Discord: https://discord.com/channels/1142723554476044338/1142723554941608006");
				printf("\n");
				system("pause");
				system("cls");
				break;
			case 2:
				//Segundo menu
				meni2();
				break;
			case 3:
				boletim();
				break;
			case 4:
				printf("\n Saindo do Sistema...");
				break;
			default:
				printf("\n Entrada Invalida!\n");
				printf("\n");
				system("pause");
				system("cls");
		}
	}while(menu1 != 4);
}

void meni2(){
	
		int menu2;
		
		do{
			printf("\n =============================\n");
			printf("\t COMUNIDADES");
			printf("\n =============================\n");
			printf("\n 1 - Empregabilidade\n");
			printf(" 2 - Notícias Tech\n");
			printf(" 3 - Trello\n");
			printf(" 4 - Github\n");
			printf(" 5 - Monitoria\n");
			printf(" 6 - Lideres\n");
			printf(" 7 - Softskills\n");
			printf(" 8 - Discord\n");
			printf(" 9 - Voltar\n");
			printf(" Qual comunidade deseja acessar: ");
			scanf("%d", &menu2);
			system("cls");
			
			switch (menu2){
				case 1:
					empregabilidade();
					break;
				case 2: 
					noticias_tech();
					break;
				case 3: 
					trello();
					break;
				case 4:
					github();
					break;
				case 5:
					monitoria();
					break;
				case 6:
					lideres();
					break;
				case 7:
					softskills();
					break;
				case 8:
					discord();
					break;
				case 9:
					meni1();
					break;	
				default:
				printf("\n Entrada Invalida!\n");
			}
		}while(menu2 != 9);		
}

void  empregabilidade(){
	
	printf(" Empregabilidade - Membros\n\n");	
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Empregabilidade", alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void noticias_tech(){
	
	printf(" Notícias Tech - Membros\n\n");
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Notícias Tech",alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void trello(){
	printf("\n Trello - Membros\n\n");
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Trello",alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void github(){
	printf("\n Github - Membros\n\n");
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Github",alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void monitoria(){
	printf("\n Monitoria - Membros\n\n");
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Monitoria",alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void lideres(){
	printf("\n Lideres - Membros\n\n");
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Lideres",alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void softskills(){
	printf("\n Softskills - Membros\n\n");
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Softskills",alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void discord(){
	printf("\n Discord - Membros\n\n");
	for(cont = 0; cont < 26; cont++){
		if(strcmp("Discord",alun[cont].comunidade) == 0){
			printf(" %s\n",alun[cont].nome);
		}
	}
	printf("\n");
	system("pause");
	system("cls");
}

void boletim(){
	
	float media[26];

	printf("\n =============================\n");
	printf("\t BOLETIM");
	printf("\n =============================\n\n");
	for(cont = 0; cont < 26; cont++){
		media[cont] = rand() % 10;
		printf(" %s | Media:%.1f\n",alun[cont].nome,media[cont]);
	}
	printf("\n");
	system("pause");
	system("cls");
}
