import is_prime
import is_prime_opt
import perfplot

pp = perfplot.live(
    setup=lambda n: n,  # 関数に与える引数を返す
    n_range=[k for k in range(1, 300)],  # テストする値の範囲を指定
    kernels=[is_prime.is_prime, is_prime_opt.is_prime],
    labels=["is_prime", "is_prime_opt"],
)
