 # long num=0;int val=n;
 #        if(n%3==0)
 #        {
 #            // while(n>0)
 #            // {num=num*10+1;n--;}
 #            // System.out.println(num*5);
 #            for (int i=0;i<n;i++) {
 #                System.out.print("5");
 #            }
 #            System.out.println();
 #            return;
 #        }
 #        else
 #        {
 #            n=val;
 #            int q=n/3;
 #            while(q>0)
 #            {
 #                if((n-(q*3))%5==0)
 #                {
 #                    int r=n-(q*3);
 #                    q=q*3;
 #                    while(q>0)
 #                    {System.out.print("5");q--;}
 #                    while(r>0)
 #                    {System.out.print("3");r--;}
 #                System.out.println();
 #                    return;
 #                }
 #                else
 #                q--;
 #            }
 #            if(val%5==0)
 #            {
 #                 while(n>0)
 #            {System.out.print("3");n--;}
 #            System.out.println();
 #            return;
 #            }
 #         System.out.println(-1);
 #        }
 #        return ;


import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    num=0
    val=n
    if n%3==0:
            print("5"*n)
            return
    else:
            q=n//3
            while q>0:
                if (n-(q*3))%5==0:
                    r=n-(q*3)
                    q=q*3
                    print("5"*q+"3"*r)
                    return;
                else:
                    q-=1
            if val%5==0:
                print("3"*n)
                return
            print("-1")


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

