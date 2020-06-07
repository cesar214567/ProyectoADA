pair<vector<Tupla>, double> cuadA[p][p][p]={0};
pair<vector<Tupla>, double> cuadB[p][p][p]={0};
pair<vector<Tupla>, double> respuestas[p][p]; //inicializar los .second con INT16_MAX;


min_peso_bloques(r,s,i,j){
    if (r == s){
        if (cuadA[r][i][j].second==INT16_MAX){
            cuadA[r][i][j].second=0;
            for(int m = i; m <= j; m++) {
                cuadA[r][i][j].first.emplace_back( r, m );
                cuadA[r][i][j].second += B[m].longitud;
            }
        }
        return make_pair ( cuadA[r][i][j].first , A[r].longitud/cuadA[r][i][j].second );

    
    }
    else if (i == j){
        if (cuadB[i][r][s]==INT16_MAX){
            cuadB[i][r][s].second=0;
            for(int m = r; m <= s; m++) {
                cuadB[i][r][s].first.emplace_back( m, i );
                cuadB[i][r][s].second += B[m].longitud;
            }
        }
        return make_pair ( cuadB[i][r][s].first , A[r].longitud/cuadB[i][r][s].second );
    }
    else{
        .
        .
        .
        for(int k = j-1; k >=i ; k--){
            auto aux_leftk = min_peso_bloques(r, r, i, k);
            auto aux_rightk = min_peso_bloques(r+1, s, k+1, j);
            resultk  = aux_leftk.second + aux_rightk.second;
            if (min_resultk > resultk ) {
                min_resultk = resultk;
                leftk = aux_leftk;
                rightk = aux_rightk;
            }
        }

        matchsk.insert( matchsk.begin(), begin(leftk.first), end(leftk.first) );
        matchsk.insert( matchsk.end(), begin(rightk.first), end(rightk.first) );

        for(int l = s-1; l >= r ; l--) {
            auto aux_leftl = min_peso_bloques(r, l, i, i);
            auto aux_rightl = min_peso_bloques(l + 1, s, i + 1, j);
            resultl = aux_leftl.second + aux_rightl.second;
            
            if (min_resultl > resultl) {
                min_resultl = resultl;
                leftl = aux_leftl;
                rightl = aux_rightl;

            }
        }

        matchsl.insert( matchsl.begin(), begin(leftl.first), end(leftl.first) );
        matchsl.insert( matchsl.end(), begin(rightl.first), end(rightl.first) );

        if( min_resultk > min_resultl ) {
            respuestas[i][j].first=matchsl;
            respuestas[i][j].second=min_resultl;
        }else{
            respuestas[i][j].first=matchsk;
            respuestas[i][j].second=min_resultk;
        }
        return respuestas[i][j];










    }





}