#include<bits/stdc++.h>
using namespace std;

/*
Leer el tamaño de un arreglo y una clave (key) de referencia desde la entrada estándar, se
guardan los elementos del arreglo y se determina la posición del elemento que coincide con la clave.
Luego, cuenta cuántos subarreglos (hacia adelante y hacia atrás desde la posición de la clave) tienen un número igual
de elementos mayores y menores que la clave.
Finalmente, imprime la cantidad de esos subarreglos que cumplen la condición.
 */
int main(){
    int tam, key;
    cin >> tam >> key;
    vector<int>arreglo(tam);
    int id = -1;
    for(int i = 0; i < tam; i++) {
        cin >> arreglo[i];
        if(arreglo[i] == key) {
            id = i;
        }
    }
    map<int, int>dif;
    int cur_dif = 0;
    for(int i = id; i < tam; i++) {
        if(arreglo[i] > key){
            cur_dif++;
        }
        if(arreglo[i] < key){
            cur_dif--;
        }
        dif[cur_dif]++;
    }
    int res = 0;
    cur_dif = 0;
    for(int i=id; i>=0; i--) {
        if(arreglo[i] > key){
            cur_dif++;
        }
        if(arreglo[i] < key) {
            cur_dif--;
        }
        res += dif[-cur_dif];
    }
    cout << res << "\n";
    return 0;
}
