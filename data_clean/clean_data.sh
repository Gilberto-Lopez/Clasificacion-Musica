sort canciones.csv | uniq > canciones_sin_repeticiones.csv
cp canciones_sin_repeticiones.csv canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C1169/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C1153/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C22/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C10/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C8/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C100007/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C24/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C12/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C1073/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C16/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C19/d' canciones_sin_repeticiones_generos_dispersos.csv
sed -i '/C7/d' canciones_sin_repeticiones_generos_dispersos.csv
grep "C14" < canciones_sin_repeticiones_generos_dispersos.csv > pop.csv
COUNTER=266
for i in `seq 1 100`;
do
  sed -i $((1 + RANDOM % $COUNTER))d pop.csv
  COUNTER=$[COUNTER-1]
done
cp canciones_sin_repeticiones_generos_dispersos.csv canciones_sin_repeticiones_generos_dispersos_pop.csv
while read -r xx;
do
  sed -i "/$xx/d" canciones_sin_repeticiones_generos_dispersos_pop.csv 
done < pop.csv
rm pop.csv