import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;

class Toy implements Comparable<Toy> {
    private String id;
    private String name;
    private double weight;

    public Toy(String id, String name, double weight) {
        this.id = id;
        this.name = name;
        this.weight = weight;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getWeight() {
        return weight;
    }

    @Override
    public int compareTo(Toy other) {
        // Compare toys based on their weights
        return Double.compare(this.weight, other.weight);
    }
}

class ToyQueue {
    private PriorityQueue<Toy> queue;

    public ToyQueue(String[] toyStrings) {
        this.queue = new PriorityQueue<>();
        for (String toyString : toyStrings) {
            String[] parts = toyString.split(",");
            String id = parts[0].trim();
            String name = parts[1].trim();
            double weight = Double.parseDouble(parts[2].trim());
            Toy toy = new Toy(id, name, weight);
            queue.add(toy);
        }
    }

    public Toy getToy() {
        return queue.poll();
    }
}

class Main {
    public static void main(String[] args) {
        String[] toyStrings = {
            "1, Машинка, 0.8",
            "2, Конструктор , 0.5",
            "3, Кукла, 0.3",
            "4, Мячик, 0.6",
            "2, Кубики , 0.2",
            "3, Пластелин, 0.1"
        };

        ToyQueue toyQueue = new ToyQueue(toyStrings);

        try (FileWriter writer = new FileWriter("output.txt")) {
            Toy toy;
            while((toy = toyQueue.getToy()) != null){
                writer.write("ID: " + toy.getId() + ", Name: " + toy.getName() + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}