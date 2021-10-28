

#print("Ceasar Brute Force")


entrada = open ('textito.txt', 'r')
salida = open ('salidita.txt','w')
mensaje = entrada.read()


abc = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z]
ABC = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z]


#mensaje_b = mensaje.swapcase
#longitud = len(mensaje)
#print(longitud)

for i in mensaje:
    print(i)
    salida.write(i)
