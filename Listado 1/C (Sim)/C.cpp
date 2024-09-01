#include <iostream>
#include <deque>
#include <string>
using namespace std;

// Backspace con "<" -> Borra el caracter anterior
// Home con "[" -> Se mueve al principio de la línea
// End con "]" -> Se mueve al final de la línea
int main() {
    int num_test_cases;
    cin >> num_test_cases;
    cin.ignore();
    for (int i = 0; i < num_test_cases; i++) {
        string inputcito;
        getline(cin, inputcito);
        deque<char> resultado;
        auto cursor = resultado.begin();
        for (char palabra : inputcito) {
            if (palabra == '<') {
                if (cursor != resultado.begin()) {
                    cursor = resultado.erase(--cursor);
                }
            } else if (palabra == '[') {
                cursor = resultado.begin();
            } else if (palabra == ']') {
                cursor = resultado.end();
            } else {
                cursor = resultado.insert(cursor, palabra);
                ++cursor;
            }
        }
        for (char c : resultado) {
            cout << c;
        }
        cout << endl;
    }
    return 0;
}