template<int I>
struct Idx { };

int i();
int up();
int get();
int load();
int parse();
int format();

struct Foo {};

template<class T>
struct InvokeResult { using Type = int; };

template<>
struct InvokeResult<int> {};

template<class T>
using InvokeResultT = typename InvokeResult<T>::Type;

template<int IDX, class T>
auto frame(T) -> InvokeResultT<T> {
}

void bad_apple()
{
|FRAMES|
}

int main()
{
    bad_apple();
}
