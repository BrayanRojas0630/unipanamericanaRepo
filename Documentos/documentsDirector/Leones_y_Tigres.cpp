#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    //Desarrollado Por: 
    // Sebastian Urrea & Johan Sanchez - Paradigmas de Programacion
    srand (time(NULL));
    char matriz[10][10];
    char prueba[10][10];
    char copia [10][10];//la que se va a comparar con la final, osea esta va a quedar como la original
    int numeroI=0, numeroJ=0;
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            matriz[i][j]='*';
            copia[i][j]='*';
            prueba[i][j]='*';
        }
    }
     
    
    int contador=0;
    for(int i=0;i<8;i++){
        
             numeroI = 1+rand()%(10-2);
             numeroJ = 1+rand()%(10-2);
             if(matriz[numeroI][numeroJ]=='T'){
                i=i-1;
             }else{
                 matriz[numeroI][numeroJ]='T';
                 copia[numeroI][numeroJ]='T';
             }
     }
     
      for(int i=0;i<8;i++){
        
             numeroI = 1+rand()%(10-2);
             numeroJ = 1+rand()%(10-2);
             if(matriz[numeroI][numeroJ]=='L'){
                i=i-1;
             }else{
                 if(matriz[numeroI][numeroJ]=='T'){
                     i=i-1;
                 }else{
                      matriz[numeroI][numeroJ]='L';
                 copia[numeroI][numeroJ]='L';
                 }
                
             }
     }
    
        
    
    
 
    for (int i=1;i<9;i++){
        for(int j=1;j<9;j++){
            if(matriz[i][j]=='T'){
                int leones=0;
                int tigres=1;
                //-----Validando los superiors 
                    if(matriz[i-1][j-1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i-1][j-1]=='L'){
                            leones++;
                        }
                    }
                    
                    if(matriz[i-1][j]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i-1][j]=='L'){
                            leones++;
                        }
                    }
                    
                    if(matriz[i-1][j+1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i-1][j+1]=='L'){
                            leones++;
                        }
                    }
                    
                //---- validando el medio
                    if(matriz[i][j-1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i][j-1]=='L'){
                            leones++;
                        }
                    }
                    
                    if(matriz[i][j+1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i][j+1]=='L'){
                            leones++;
                        }
                    }
                    
                //------- validando inferiores
                    if(matriz[i+1][j-1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i+1][j-1]=='L'){
                            leones++;
                        }
                    }
                    
                    if(matriz[i+1][j]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i+1][j]=='L'){
                            leones++;
                        }
                    }
                    
                    if(matriz[i+1][j+1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i+1][j+1]=='L'){
                            leones++;
                        }
                    }
                    
                    if(leones>tigres){
                        matriz[i][j]='*';
                        
                    }
                
                       
            }//---------validando con los leones-----------------------
            else{
                if(matriz[i][j]=='L'){
                    int leones=1;
                    int tigres=0;
                //-----Validando los superiors 
                    if(matriz[i-1][j-1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i-1][j-1]=='L'){
                            leones++;
                        }
                    }
                    if(matriz[i-1][j]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i-1][j]=='L'){
                            leones++;
                        }
                    }
                    if(matriz[i-1][j+1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i-1][j+1]=='L'){
                            leones++;
                        }
                    }
                //---- validando el medio
                    if(matriz[i][j-1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i][j-1]=='L'){
                            leones++;
                        }
                    }
                    if(matriz[i][j+1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i][j+1]=='L'){
                            leones++;
                        }
                    }
                //------- validando inferiores
                    if(matriz[i+1][j-1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i+1][j-1]=='L'){
                            leones++;
                        }
                    }
                    if(matriz[i+1][j]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i+1][j]=='L'){
                            leones++;
                        }
                    }
                    if(matriz[i+1][j+1]=='T'){
                        tigres++;
                    }else{
                        if(matriz[i+1][j+1]=='L'){
                            leones++;
                        }
                    }
                    
                    if(tigres>leones){
                        matriz[i][j]='*';
                        
                    }
                     
                }
                
                    
            }
            
        }
    }
    
    
    printf("Copiaaaaa Original %d\n",contador);
      for(int i=1;i<9;i++){
            for(int j=1;j<9;j++){
                printf(" %c", copia[i][j]);
            }
            printf("\n");
       }
       printf("Cambiado\n");
    
        for(int i=1;i<9;i++){
            for(int j=1;j<9;j++){
                printf(" %c", matriz[i][j]);
            }
            printf("\n");
        } 
        return 0;
    }

 