#!/usr/bin/python3

'''
    ===========================================================================================================
    This project was inspired by this post: https://bitcoinmagazine.com/culture/diy-bitcoin-private-key-project
    ===========================================================================================================
'''


from hashlib import sha256
def format_str(value):
    '''
     ===Only pass <class 'str'> to this function===
     Truncates the first two characters so that 
     (e.g) 0b1100001 becomes 1100001 or 0x61 becomes 61
     and reurns the result as a <class 'str'>
    '''
    return value[2:]

#============================================================================================================#

# The 2048 english word list is hosted at: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
# Download into the same local directory as this script
# Use the cli command: wget https://github.com/bitcoin/bips/raw/master/bip-0039/english.txt
# Advice: make the local file 'read only'

def get_word(word):
    f = open("english.txt", "r")
    for read in range(word+1): # We need to add 1 becasue, unlike a list or an array, a text file does not start at line zero.
        bip39 = (f.readline())
    f.close()
    return(bip39[:-1]) # Remove the '\n' from the end of the word before returning it.
#============================================================================================================#


print('\n The input needs to be 64 (at least) random hexadecimal characters\n') 
to_hash = input(' HEX Number: ')

if len(to_hash) < 64:
    print('Warning: your input is less then 64 characters long which puts your key at risk.')

if len(to_hash) %2 == 0:

    # HEX to BIN converter
    scale = 16 ## equals to hexadecimal
    bit_depth = 256
    num_of_bits = len(bin(int(to_hash, scale))[2:].zfill(bit_depth))
  
    
    key = (sha256(bytearray.fromhex(to_hash)).hexdigest())

    print('\n The word list will be derived from this key\n\n','HEX...',key)
    
    dec_out = int(key, 16)
    print('\n Decimal...',dec_out)
    bin_key_string = str(bin(int(key, scale))[2:].zfill(bit_depth))
    print('\n Binary...',bin(int(key, scale))[2:].zfill(bit_depth))
    print(len(bin_key_string),'bit length')
    
    # ============================================================================= #
    # Get the check sum and generate the 8 bit binary needed for the 24th Seed Word #
    get_hash      = sha256(bytearray.fromhex(key)).hexdigest()
    get_hash_byte = (bytearray.fromhex(get_hash[:2]))
    get_hash_dec  = int(get_hash_byte[0])
    
    # If less than 8 bits in length, this needs to padded with leading zeros
    bin_out = (format_str(bin(get_hash_dec)))
    word_file = "word_list.txt" #This is the file name that will contain the seed words.
    pad = []
    pad_string = ''
    if len(bin_out) < 8:
        padding = 8-len(bin_out)
        for loop in range(padding):
            pad.append('0')
    pad.append(format_str(bin(get_hash_dec)))
    
    for bits in pad:
        pad_string += bits
    
    print('\nThe binary code needed for the 24th BIP0039 Seed Word\n',(pad_string))
    # ============================================================================= #
        
    print('\nThe 24 BIP0039 Seed Words...\n')
    print('Pos','\t','Bin Num','\t','Dec Num','\t','Word\n')
    
    start = 0
    end   = 11
    for loop in range(24):
        bin_num = (bin_key_string[start:end])
        if loop < 23:
            print(loop+1,'\t',bin_num,'\t',int(bin_num,2),'\t','\t',get_word(int(bin_num,2)))
            f = open(word_file, "a")
            f.write((get_word(int(bin_num,2))))
            f.write(" ")
            f.close()        
        else: # Build the 24th Seed Word and continue
            bin_num = (bin_key_string[-3:]+pad_string)
            print(loop+1,'\t',bin_num,'\t',int(bin_num,2),'\t','\t',get_word(int(bin_num,2)))
            f = open(word_file, "a")
            f.write((get_word(int(bin_num,2))))
            f.write("\n\n")
            f.close() 
        start +=11
        end   +=11
    
    print('\nEnd of script')
else:
    print(' Error in HEX input')
