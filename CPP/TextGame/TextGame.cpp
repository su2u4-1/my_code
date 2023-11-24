#include <iostream>
#include <string>
#include <list>
using namespace std;

list<string> LocationList;

class BuildRoles{
public:
    string name;
    string location = "一個空空的白色房間";
    int atk = 10;
    int def = 10;
    int hp = 100;
    int mp = 100;
    int luck = 50;

    BuildRoles(string n){
        BuildRoles::name = n;
    }

    void ChangeLocation(string l){
        BuildRoles::location = l;
        LocationList.emplace_back(l);
        cout << "\n你現在的位置在" << l << endl;
    }

    void GoBack(){
        string l = LocationList.back();
        BuildRoles::location = l;
        LocationList.pop_back();
        cout << "\n你現在的位置在" << l << endl;
    }
};

int main(){
    string name;
    cout << "歡迎遊玩文字遊戲" << endl;

    while(true){
        string a;
        name = "Foobar";
        cout << "\n請輸入角色名字:";
        cin >> name;
        cout << "\n你的名字是" << name << "\n\n確定要用這個名字了嗎 (y)/(n):";
        cin >> a;
        if(a == "y" || a == "Y" || a == "yes" || a == "Yes"){
            break;
        }
    }

    BuildRoles player(name);
    cout << "\n接下來請分配你的角色能力值\n角色的能力值共有5種，分別是力量、耐力、體力、精神和幸運\n你可分配的點數有25點，分配方式是分別把要加給5種能力值的點數數量分別用空白鍵分開\n例如:5 5 5 5 5\n此例即是平均分配" << endl;
    
    while(true){
        string a;
        int ability0,ability1,ability2,ability3,ability4;
        cout << "\n請輸入要分配的能力值:";
        try{
            cin >> ability0 >> ability1 >> ability2 >> ability3 >> ability4;
        }catch(...){
            cout << "\n你的輸入有問題" << endl;
            continue;
        }
        if(ability0+ability1+ability2+ability3+ability4 > 25){
            cout << "\n你的輸入超過上限" << endl;
            continue;
        }else if(ability0+ability1+ability2+ability3+ability4 < 25){
            cout << "\n你的可分配點數還有剩餘\n請問要重新分配嗎? (y)/(n):";
            cin >> a;
            if(a == "n" || a == "N" || a == "no" || a == "No"){
                player.atk = ability0*2;
                player.def = ability1*2;
                player.hp = ability2*20;
                player.mp = ability3*20;
                player.luck = ability4*10;
                break;
            }else{
                continue;
            }
        }else{
            cout << "\n你的能力值\n力量:" << ability0*2 << "耐力:" << ability1*2 << "體力:" << ability2*20 << "精神:" << ability3*20 << "幸運:" << ability4*10 << "\n確定要用這種分配了嗎 (y)/(n):";
            cin >> a;
            if(a == "y" || a == "Y" || a == "yes" || a == "Yes"){
                player.atk = ability0*2;
                player.def = ability1*2;
                player.hp = ability2*20;
                player.mp = ability3*20;
                player.luck = ability4*10;
                break;
            }
        }
    }

    cout << "\n歡迎來到天玄大陸" << endl;
    player.ChangeLocation("天玄大陸-中土-新手村口");

    while(true){

        while(player.location == "天玄大陸-中土-新手村口"){
            int option;
            cout << "\n1.逛逛村子 2.出去打怪 3.打開系統:";
            try{
                cin >> option;
            }catch(...){
                cout << "\n你的輸入有問題" << endl;
                continue;
            }
            switch(option){
                case  1:
                    player.ChangeLocation("天玄大陸-中土-新手村內");
                    break;
                case 2:
                    player.ChangeLocation("天玄大陸-中土-新手村外");
                    break;
                case 3:
                    player.ChangeLocation("系統介面");
                    break;
                default:
                    cout << "\n你的輸入有問題" << endl;
                    continue;
            }
        }
        
        while(player.location == "天玄大陸-中土-新手村內"){
            int option;
            cout << "\n1.村長家 2.雜貨舖 3.鐵匠鋪 4.草藥鋪 5.銀行 6.布告欄 7.離開 8.系統:";
            try{
                cin >> option;
            }catch(...){
                cout << "\n你的輸入有問題" << endl;
                continue;
            }
            switch(option){
                case 1:
                    player.ChangeLocation("天玄大陸-中土-新手村-村長家");
                    break;
                case 2:
                    player.ChangeLocation("天玄大陸-中土-新手村-雜貨舖");
                    break;
                case 3:
                    player.ChangeLocation("天玄大陸-中土-新手村-鐵匠鋪");
                    break;
                case 4:
                    player.ChangeLocation("天玄大陸-中土-新手村-草藥鋪");
                    break;
                case 5:
                    player.ChangeLocation("天玄大陸-中土-新手村-銀行");
                    break;
                case 6:
                    player.ChangeLocation("天玄大陸-中土-新手村-布告欄");
                    break;
                case 7:
                    player.ChangeLocation("天玄大陸-中土-新手村外");
                    break;
                case 8:
                    player.ChangeLocation("系統介面");
                    break;
                default:
                    cout << "\n你的輸入有問題" << endl;
                    continue;
            }
        }

        while(player.location == "天玄大陸-中土-新手村外"){
            int option;
            cout << "\n1. 2. 3.打開系統:";
            try{
                cin >> option;
            }catch(...){
                cout << "\n你的輸入有問題" << endl;
                continue;
            }
            switch(option){
                case  1:
                    player.ChangeLocation("");
                    break;
                case 2:
                    player.ChangeLocation("");
                    break;
                case 3:
                    player.ChangeLocation("系統介面");
                    break;
                default:
                    cout << "\n你的輸入有問題" << endl;
                    continue;
            }
        }
    }
    return 0;
}