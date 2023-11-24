#include <iostream>
using namespace std;

int main() {
    while(true){
        int a = 0;
        int i = 2;
        cout << "判斷是否是質數，請輸入數字，輸入0結束程式:";
        cin >> a;
        if(a == 0){
            break;
        }
        else if(a <= 1){
            cout << "不可輸入小於等於1的數\n" << endl;
        }
        else{
            for(i = 2;i < a;i++){
                if(a%i == 0){
                    cout << a << "不是質數\n" << endl;
                    break;
                }
            }
            if(i == a){
                cout << a << "是質數\n" << endl;
            }
        }
    }
    return 0;
}