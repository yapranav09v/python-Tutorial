#include<iostream>
using namespace std;

class Arithmatic
{
    public:
    double num1, num2;
    int number;
    char choice;

    void cal_getdat()
    {
        cout<<"\nEnter the two numbers:- ";
        cin>>num1>>num2;

        cout<<"Enter the operation:- ";
        cin>>choice;

        switch (choice)
        {
        case '+':
            cout<<"The addition is:- "<<num1+num2;
            break;

        case '-':
            cout<<"The substration is:- "<<num1-num2;
            break;

        case '*':
            cout<<"The multiplication is:- "<<num1*num2;
            break;

        case '/':
            cout<<"The division is:- "<<num1/num2;
            break;
        
        default:
            cout<<"Invalid Operator!";
            break;
        }
    }

    void num_table()
    {
        cout<<"Enter the number to find it's Table:- ";
        cin>>number;
        for(int i=1; i<=10; i++)
        {
            cout<<"\n"<<i*number<<endl;
        }
    }
};

int main()
{
    while(true)
    {
    int ch;
    cout<<"\n\n1 for calculator and 2 for any number table\n";
    cout<<"\nEnter the choice:- ";
    cin>>ch;
   Arithmatic myobj;

   if(ch==1)
   {
   myobj.cal_getdat();
   }
   if(ch == 2)
   {
    myobj.num_table();
   }
    }
}
   
