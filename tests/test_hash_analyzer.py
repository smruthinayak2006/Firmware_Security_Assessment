import sys
import os

sys.path.append(
    os.path.abspath("analysis")
)


from hash_analyzer import calculate_hash




def test_hash_generation():


    test_file = "tests/sample.txt"




    with open(

        test_file,

        "w"

    ) as file:


        file.write(

            "firmware test"

        )





    result = calculate_hash(

        test_file

    )




    assert result["md5"] != ""

    assert result["sha256"] != ""





    os.remove(

        test_file

    )