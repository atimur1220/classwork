#include <iostream>
#include <cmath>
using namespace std;

void pat(){
    cout<<"Lungimea unei laturi (cm): ";
    double pLat; 
    cin>>pLat;
    double ariaP = pow(pLat, 2);

    if(pLat < 0){
        cout<<"eroare!!(date invalide)";
    } else {
        cout<<"Aria patratului = "<<ariaP<<" cm^2";       
    }
}

void drep(){
    cout<<"Lungimea dreptunghiului(cm): ";
    double dLung;
    double dLat;
    cin>>dLung;
    cout<<"Latimea dreptunghiului(cm): ";
    cin>>dLat;
    double ariaD = dLung * dLat;
    if(ariaD < 0){
        cout<<"eroare!!(date invalide)";
    } else {
        cout<<"Aria dreptunghiului = "<<ariaD<<" cm^2";
    }
}


void cer(){
    const double pi = 3.1415926535;
    cout<<"Raza cercului(cm): ";
    double Raza;
    cin>>Raza;
    double cLung = 2 * pi * Raza;
    double RazaP = pow(Raza, 2);
    double ariaC = pi * RazaP;
    if(cLung < 0){
        cout<<"eroare!! (date invalide)";
    } else {
        cout<<"Lungimea cercului = "<<cLung<<" cm"<<endl;
        cout<<"Aria cercului = "<<ariaC<<" cm^2";
    }

}

int main(){
    cout<<"(1 - Patrat; 2 - Dreptunghi; 3 - Cerc): ";
    int al;
    cin>>al;
    switch(al){
        case 1:
            pat();
            break;
        case 2:
            drep();
            break;
        case 3:
            cer();
            break;
    }
    return 0;
}
