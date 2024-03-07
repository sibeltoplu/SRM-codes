reset()
forget(assumptions())

# Define the variables
x,y,z = var('x y z')

# Define the expression T
a,b,c,d, e, f, g, h, i = var('a b c d e f g h i')

X = a*x+b*y+c*z
Y = d*x+e*y+f*z
Z = g*x+h*y+i*z

D1 = matrix([[1,1,1],[X,Y,Z],[X^2,Y^2,Z^2]]).determinant()
D1s = (D1.full_simplify())

D2 = matrix([[1,1,1],[X,Y,Z],[X^3,Y^3,Z^3]]).determinant()
D2s = (D2.full_simplify())
#print(D1s)

eqns1 = [D1s.coefficient(x*y*z),D1s.coefficient(x^3),D1s.coefficient(y^3),D1s.coefficient(z^3),D1s.coefficient(x*y^2)+D1s.coefficient(x^2*y),D1s.coefficient(z*y^2)+D1s.coefficient(z^2*y),D1s.coefficient(x*z^2)+D1s.coefficient(x^2*z)]
#show(eqns1)

eqns2 = [D2s.coefficient(x*y*z^2),D2s.coefficient(x*y^2*z),D2s.coefficient(x^2*y*z),D2s.coefficient(x^2*y^2),D2s.coefficient(x^2*z^2),D2s.coefficient(z^2*y^2),D2s.coefficient(x^4),D2s.coefficient(y^4),D2s.coefficient(z^4),D2s.coefficient(x*y^3)+D2s.coefficient(x^3*y),D2s.coefficient(z*y^3)+D2s.coefficient(z^3*y),D2s.coefficient(x*z^3)+D2s.coefficient(x^3*z)]
#show(eqns2)

eqns = eqns1+eqns2

print("----------------------------------------------------------------------------------------------------")

# for eq in eqns:
#     show(eq)
#     #print(eq(a=2,b=1,c=1,d=1,e=2,f=1,g=1,h=1,i=2))
#     print("----------------------------------------------------------------------------------------------------")

    
det=matrix([[a,b,c],[d,e,f],[g,h,i]]).determinant()

sol = solve([eqns[1]==0,eqns[2]==0,eqns[13]==0,eqns[14]==0,eqns[4]==0,eqns[16]==0],a,b,d,e,g,h)
#print(sol)
sol_dict = solve([eqns[1]==0,eqns[2]==0,eqns[13]==0,eqns[14]==0,eqns[4]==0,eqns[16]==0],a,b,d,e,g,h,solution_dict=True)

# #sol=solve([eqns[1],eqns[13]],a,d,g)
# sol = solve([eqns[1]==0,eqns[2]==0,eqns[3]==0,eqns[13]==0,eqns[14]==0,eqns[15]==0,eqns[4]==0,eqns[16]==0],a,b,c,d,e,f,g,h,i)
# sol_dict = solve([eqns[1]==0,eqns[2]==0,eqns[3]==0,eqns[13]==0,eqns[14]==0,eqns[15]==0,eqns[4]==0,eqns[16]==0],a,b,c,d,e,f,g,h,i,solution_dict=True)
# #sol= solve(eqns,a,b,c,d,e,f,g,h,i) 
# #print(len(sol),sol)

eqns_ex = [eqns[0],eqns[3],eqns[15]]+eqns[5:13]+eqns[17:19]

for j in range(len(sol_dict)):
    if ((det(sol_dict[j])).full_simplify())!=0:
        print(j,sol_dict[j])
        sol_g = solve(eqns_ex+sol[j],a,b,c,d,e,f,g,h,i,solution_dict=True)
        #print(sol_g)
        for k in range(len(sol_g)):
            if ((det(sol_g[k])).full_simplify())!=0:
                print(j,k,sol_g[k])
                print("----------------------------------------------------------------------------------------------------")

#         #eqns_ex_subt=[eqns_ex[k](sol[j]) for k in range(len(eqns_ex))]
#         #print(eqns_ex_subt[0])
#         #print(solve(eqns_ex_subt,a,b,c,d,e,f,g,h,i))

# #sol_p = [e==a,i==a,c==b,d==b,f==b,g==b,h==b]
# #solve(eqns+sol_p,a,b,c,d,e,f,g,h,i)
