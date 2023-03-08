# Wprowadzenie do TSPLIB

1. **Format pliku** - każdy plik składa się z dwóch części: specyfikacji oraz danych. Część specyfikacji zawiera informacje o formacie pliku i jego zawartości.
2. **Część specyfikacji** - każde pole słada się z dwóch wartości: \<keyword> : \<value>
    1. NAME : \<string> - określa nazwę pliku z danymi
    2. TYPE : \<string> - określa typ danych
        * TSP - symetryczny problem komiwojażera
        * ATSP - asymetryczny problem komiwojażera
    3. COMMENT : \<string> - dodatkowe komentarze
    4.   DIMENSION : \<integer> - dla TSP lub ATSP wymiar (ang. ***dimension***) to liczba wierzchołków.
    5. EDGE_WEIGHT_TYPE : \<string> - określa typ podanych krawędzi
        * EXPLICIT - wagi są sprecyzowane
        * EUC_2D - wagi są odległościami euklidesowymi w 2D
        * EUC_3D - wagi są odległościami euklidesowymi w 3D
    6. EDGE_WEIGHT_FORMAT : \<string> - określa format w jakim podane są krawędzie (dotyczy typu EXPLICIT)
        * FUNCTION - wagi są podane w sposób funkcji
        * FULL_MATRIX - wagi są podane jako pełna macierz
        * UPPER_ROW - wagi są zapisane w macierzy trójkątnej (górnej, według rzędów, bez wartości diagonalnych)
        * LOWER_ROW - wagi są zapisane w macierzy trójkątnej (dolnej, według rzędów, bez wartości diagonalnych
        * UPPER_DIAG_ROW - wagi są zapisane w macierzy trójkątnej (górnej, według rzędów, z wartościami diagonalnymi)
        * LOWER_DIAG_ROW - wagi są zapisane w macierzy trójkątnej (dolnej, według rzędów, z wartościami diagonalnymi)
    7. EDGE_DATA_FORMAT : \<string> - określa format w jakim podane są krawędzie w grafie
        * EDGE_LIST - graf jest podany jako lista krawędzi
        * ADJ_LIST - graf jest podany jako lista sąsiedztwa
    8. NODE_COORD_TYPE - określa koordynaty przypisane do każdego wierzchołka
        * TWOD_COORDS - wierzchołki mają koordynaty 2D
        * THREED_COORDS - wierzchołki mają koordynaty 3D
        * NO_COORDS - wierzchołki nie mają przypisanych koordynat
    9. EOF - kończy dane wejściowe (opcjonalnie)


