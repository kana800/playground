set(CARD_SOURCE_FILE
    bronzecard.h
    creditcard.h
    goldcard.h
    silvercard.h
    offervisitor.h
)

add_library(card ${CARD_SOURCE_FILE})

set_target_properties(card PROPERTIES LINKER_LANGUAGE CXX)