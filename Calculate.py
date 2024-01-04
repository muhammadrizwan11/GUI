import streamlit as st
import pandas as pd

def calculate_function_points(user_inputs, user_outputs, inquiries, files, external_interfaces,
                              effort, tech_documents, user_documents, cost_per_month, complexity_factors):
    count_total = user_inputs + user_outputs + inquiries + files + external_interfaces
    total_factor = count_total * 1.08  # Assuming sum of processing complexity factors

    function_points = total_factor * (0.65 + 0.01 * sum(complexity_factors))

    total_docs = tech_documents + user_documents
    documentation_ratio = total_docs / function_points
    productivity = function_points / effort
    cost_per_function = cost_per_month / productivity

    return function_points, total_docs, documentation_ratio, productivity, cost_per_function

def main():
    st.title("Function Point Calculator")

    user_inputs = st.number_input("Number of User Inputs:")
    user_outputs = st.number_input("Number of User Outputs:")
    inquiries = st.number_input("Number of Inquiries:")
    files = st.number_input("Number of Files:")
    external_interfaces = st.number_input("Number of External Interfaces:")
    effort = st.number_input("Effort (p-m):")
    tech_documents = st.number_input("Technical Documents (pages):")
    user_documents = st.number_input("User Documents (pages):")
    cost_per_month = st.number_input("Cost Per Month:")

    # Take complexity factors from the user as input
    complexity_factors = st.text_input("Enter 14 Complexity Factors (comma-separated):")
    complexity_factors = [int(factor.strip()) for factor in complexity_factors.split(',') if factor.strip()]

    # Check if the list is empty or not
    if not complexity_factors or len(complexity_factors) != 14:
        st.error("Please enter 14 valid Complexity Factors.")
    else:
        # Display Complexity Factors as an array
        # st.write("Complexity Factors:", complexity_factors)

        # Create a DataFrame with user inputs and complexity factors
        user_data = pd.DataFrame({
            "Parameter": ["User Inputs", "User Outputs", "Inquiries", "Files", "External Interfaces", "Effort",
                          "Technical Documents", "User Documents", "Cost Per Month"] + [f"Complexity Factor {i + 1}" for i in range(14)],
            "Count": [user_inputs, user_outputs, inquiries, files, external_interfaces, effort,
                      tech_documents, user_documents, cost_per_month] + complexity_factors,
            "Weighing Factor": [0] * (9 + 14)  # Initialize weighing factor to 0
        })

        # Bar chart of all user inputs
        st.bar_chart(user_data.set_index("Parameter")["Count"])

        if st.button("Calculate"):
            try:
                function_points, total_docs, documentation_ratio, productivity, cost_per_function = calculate_function_points(
                    user_inputs, user_outputs, inquiries, files, external_interfaces,
                    effort, tech_documents, user_documents, cost_per_month, complexity_factors
                )

                st.write(f"Function Points: {function_points:.2f}")
                st.write(f"Total Documentation (pages): {total_docs:.2f}")
                st.write(f"Documentation Ratio: {documentation_ratio:.2%}")
                st.write(f"Productivity: {productivity:.2f}")
                st.write(f"Cost Per Function: ${cost_per_function:.2f}")

                st.write("\nUser Input DataFrame:")
                st.write(user_data)

            except ValueError as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
