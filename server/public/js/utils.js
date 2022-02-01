function hashPassword(password, email) {
    let passwordBinary = sjcl.codec.utf8String.toBits(password);
    let emailBinary = sjcl.codec.utf8String.toBits(email);

    let emailHashedBinary = sjcl.hash.sha256.hash(emailBinary);
    let saltBinary = emailHashedBinary.slice(0, 4);
    
    /* PBKDF2 parameters
     * -----------------
     * Need to make sure these same parameters are used on client side
     * 
     * salt: 16 bytes from email
     * iterations: 100,000
     * length: 32 bytes
     * hmac_hash: sha256
     */
    let hashBinary = sjcl.misc.pbkdf2(passwordBinary, saltBinary, 100000, 256, sjcl.misc.hmac);
    let hash = sjcl.codec.base64.fromBits(hashBinary);
    return hash;
}