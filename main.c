#include <stdio.h>
#include <string.h>
#include <locale.h>
#include "discord.h"

int main(){
	setlocale(LC_ALL,"Portuguese");
	int menu1, menu2,cont;

	printf("=============================\n");
	printf("\tDISCORD");
	printf("\n=============================\n");
	printf("1 - Acessar Link\n");
	printf("2 - Acessar Comunidades\n");
	printf("3 - Acessar Boletim\n");
	printf("Escolha uma opção do menu: ");
	scanf("%d", &menu1);
	system("cls");
	
	//Opções do primeiro menu (Link,Comunidades, Boletim)
	switch (menu1){
		case 1:
			puts("Link para acessar o Discord: https://discord.com/channels/1142723554476044338/1142723554941608006");
			break;
		case 2:
			//Opções do segundo menu
			printf("1 - Empregabilidade\n");
			printf("2 - Notícias Tech\n");
			printf("3 - Trello\n");
			printf("4 - Github\n");
			printf("5 - Monitoria\n");
			printf("6 - Lideres\n");
			printf("7 - Softskills\n");
			printf("8 - Discord\n");
			printf("Qual comunidade deseja acessar: ");
			scanf("%d", &menu2);
			system("cls");
			switch (menu2){
				case 1:
					printf("Empregabilidade - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Empregabilidade",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
				case 2: 
					printf("Notícias Tech - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Notícias Tech",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
				case 3: 
					printf("Trello - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Trello",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
				case 4:
					printf("Github - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Github",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
				case 5:
					printf("Monitoria - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Monitoria",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
				case 6:
					printf("Lideres - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Lideres",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
				case 7:
					printf("Softskills - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Softskills",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
				case 8:
					printf("Discord - Membros\n");
					for(cont = 0; cont < 26; cont++){
						if(strcmp("Discord",alun[cont].comunidade) == 0){
							printf("%s\n",alun[cont].nome);
						}
					}
					break;
			}
			break;
	}
	return 0;
}


