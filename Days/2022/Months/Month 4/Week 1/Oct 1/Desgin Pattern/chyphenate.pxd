cdef exterent "hyphen.h":
    ctypedef struct HyphenDict:
        pass
    
    HyphenDict *hnj_hyphen_load(char, *filename)
    void hnj_hyphen_free(HyphenDict *hdict)
    int hnj_hyphen_hyphenate2(HyphenDict *hdict, char *word),
        int word_size, char *hyphens, char *hyphenated_word,
        char ***rep, int, ***pos, int, ***count