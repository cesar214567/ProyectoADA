result:
	g++ -o result.out ResultMinMatching.cpp
vector:
	g++ -o vector.out VectorMinMatching.cpp
memoized:
	g++ -o memoized.out MemoizedMinMatching.cpp
clean:
	rm *.out
