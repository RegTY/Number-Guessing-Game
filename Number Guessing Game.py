/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <conio.h>

int main()
{
    int answer;
    int userAnswer;
    printf("Enter a number:");
    scanf("%i", &answer );
    //clrscr();
    system("cls");

    printf("Guess my number:");
    scanf("%i", &userAnswer);
    int attempts = 1;
    while (userAnswer != answer && attempts !=5){
        int difference = userAnswer - answer;
        attempts ++;
        if (userAnswer > answer && difference <= 10 && difference > 0){
            printf("The number is lower! Your answer is very close! Try again!:");
            scanf("%i", &userAnswer);
        }
        else if (userAnswer == 1337){
            printf("You entered the cheat code, here is the answer: %i", answer);
            scanf("%i", &userAnswer);
         }
        else if (userAnswer < answer && difference < 0 && difference >= -10){
            printf("he number is higher, you are very close! Try again! ");
            scanf("%i", &userAnswer);
        }
        if (userAnswer < answer){
            printf("The number is higher! Try again! :");
            scanf("%i", &userAnswer);
        }
        else if (userAnswer > answer){
            printf("The number is lower, Try again!:");
            scanf("%i", &userAnswer);
        }
    }
    if (attempts == 5){
        printf("You ran out of attempts!");
    }
    if (userAnswer == answer){
        printf("You guessed the correct number!");
    }
}
