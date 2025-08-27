import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test
    void testAddition() {
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    void testDivision() {
        assertEquals(2, calc.divide(6, 3));
    }

    @Test
    void testDivisionByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calc.divide(5, 0);
        });
    }
}