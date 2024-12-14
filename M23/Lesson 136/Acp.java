import java.util.Scanner;

 class Main 
{
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) 
	{
		System.out.print("enter student name: ");
		String name = sc.nextLine();

		System.out.print("enter number of subjects: ");
		int no = sc.nextInt();

		/*-- create an integer array to store no subject marks --*/
		int[] marks = new int[no];

		marksEntry(marks); //method call

		printReportCard(name, marks, no); //method call
	}

	/*---- method for marks entry ---*/
	static void marksEntry(int[] marks){
		for(int i=0;i<marks.length;i++){
			System.out.print("enter mark for Subject-"+(i+1)+": ");
			marks[i] = sc.nextInt();
		}
	}

	/*---- method for generating report card ---*/
	static void printReportCard(String name, int[] marks, int no){
		System.out.println("---------------------------------------");
		System.out.println("\t REPORT CARD");
		System.out.println("NAME: "+name);
		System.out.println("---------------------------------------");

		System.out.println("  SUBJECT \t MARK");
		System.out.println("---------------------------------------");
		
		int total = 0;

		for(int i=0;i<marks.length;i++){
			System.out.println("Subject-"+(i+1)+"\t  "+ marks[i]);
			total += marks[i];
		}
		System.out.println("---------------------------------------");

		float avg = ((float)total) / no;
		//System.out.println("TOTAL: "+total+"\tAVERAGE: "+avg);
	    System.out.printf("TOTAL: %d \tAVERAGE: %.2f \n", total,avg);
		System.out.println("---------------------------------------");
	}
}
