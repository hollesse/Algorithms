import java.util.*; 

public class Example14 { 

    static <S, T extends S> T writeAll(List<T> src, Sink<S> snk) {
        T last = null;
        for (T t: src) {
            last = t;
            snk.flush(last);
        }
        return last;
    }

    public static void main(String[] args) { 
        Sink<Object> s  = new Sink();
        List<String> sl = new LinkedList<String>();
        String str = writeAll(sl, s); // T = String, S = Object
    }
}

class Sink<T> {
    void flush(T t) {
	// more code here
    }
}
