sample: sample.cu
	nvcc $^ -I ../include -L ../lib -o $@ \
		-lvqcsim_static -lcppsim_static -lcsim_static -lgpusim_static -D _USE_GPU -lcublas -Xcompiler -fopenmp

