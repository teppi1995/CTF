import java.io.InputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.security.MessageDigest;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;



public class Main{
	public static void main(String[] args) throws IOException,  NoSuchAlgorithmException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException, NoSuchPaddingException, InvalidAlgorithmParameterException{
	  FileInputStream inputStream = new FileInputStream("jewel_c.png");
	  byte[] arrayOfByte = new byte[inputStream.available()];
	  inputStream.read(arrayOfByte);
	  
	  String str = "999999913371337";
	  SecretKeySpec secretKeySpec = new SecretKeySpec(("!" + str).getBytes("ASCII"), "AES");
	  IvParameterSpec ivParameterSpec = new IvParameterSpec("kLwC29iMc4nRMuE5".getBytes());
   	  Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
	  cipher.init(2, secretKeySpec, ivParameterSpec);
	  arrayOfByte = cipher.doFinal(arrayOfByte);
	  
	  FileOutputStream outputStream = new FileOutputStream("jewel_d.png");
	  outputStream.write(arrayOfByte);
  }
}
