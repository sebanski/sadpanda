/////////////////////////////////////
//        
//        aes encryption
//        
//             __     __
//            /  \ ^ /  \
//            \ /  |  \ /
//             | . | . |
//              \__A__/
//        .|.   /  |  \   .|.
//          \+<|   |   |>+/
//              \ /|\ /
//               V===V
//              ||   ||
//           __//     \\__
//           ===		 ===
//        
//        		 sadpanda
//        
//////////////////////////////////////

type iAES struct {
	item_id UUID
	salt String
	encrypted_item String
}

func (a *iAES) encrypt(item String, ket String, salt String) String {
	// TODO: implement this method and fix the whole intro piece..
}

func (a *iAES) decrypt(item String, ket String, salt String) String {
	// TODO: implement this method and fix the whole intro piece..
}

func multiple_16(item String) String {
	// TODO: implement this feature....
}

func check_key(key String) String {
	// TODO: implement this feature....
}

func check_salt(salt String) String {
	// TODO: implement this feature....
}

func generate_salt() String {
	// TODO: implement this feature....
}

