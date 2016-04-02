import java.io.*;
import java.lang.*;
import java.nio.charset.Charset;
import java.nio.file.*;

public class SentenceSplitter {
	
		// static String readFile(String path, Charset encoding) throws IOException {
		// 	byte[] encoded = Files.readAllBytes(Paths.get(path));
		//   	return new String(encoded, encoding);
		// }

	public static void main(String[] args) {

		try{
			//String rawSentences = readFile("hunchback_english.txt", Charset.forName("ISO-8859-1"));
			// PrintWriter out = new PrintWriter("hunchback_english_sentences.txt");
			// out.println(rawSentences);
			// out.close();
			final byte NEWLINE = (byte) '\n';
			FileInputStream fs = new FileInputStream("hunchback_english.txt");
			FileOutputStream os = new FileOutputStream("hunchback_english_sentences.txt");
			byte b;
			char c;
			while((b=(byte)fs.read())!=-1) {
				c = (char)b;
				if (c != '\n') {
					os.write(c);
				} 
				if (c=='.'){
					os.write(NEWLINE);
				}
			}
			//System.out.println(rawSentences);

			// FileInputStream input = new FileInputStream("hunchback_english.txt");
			// PrintWriter output = new PrintWriter("hunchback_english_sentences.txt");

			// byte b;
			// char c;
			// while((b=(byte)input.read())!=-1) {
			// 	c = (char)b;
			// 	if (c!='\n') {
			// 		output.print(c);
			// 	}
			// 	else {
			// 		System.out.println("New Line" + c);
			// 	}
			// 	if (c=='.') {
			// 		output.println();
			// 	}
			// }



		} catch(Exception e){
			e.printStackTrace();
		}
	}
}