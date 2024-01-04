import streamlit as st

def calculate_function_points(
    user_inputs, user_outputs, inquiries, files, external_interfaces,
    effort, tech_documents, user_documents, cost_per_month
):
    count_total = user_inputs + user_outputs + inquiries + files + external_interfaces
    total_factor = count_total * 1.08  # Assuming sum of processing complexity factors

    function_points = total_factor * (0.65 + 0.01 * 43)

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

    if st.button("Calculate"):
        try:
            function_points, total_docs, documentation_ratio, productivity, cost_per_function = calculate_function_points(
                user_inputs, user_outputs, inquiries, files, external_interfaces,
                effort, tech_documents, user_documents, cost_per_month
            )

            st.write(f"Function Points: {function_points:.2f}")
            st.write(f"Total Documentation (pages): {total_docs:.2f}")
            st.write(f"Documentation Ratio: {documentation_ratio:.2%}")
            st.write(f"Productivity: {productivity:.2f}")
            st.write(f"Cost Per Function: ${cost_per_function:.2f}")

        except ValueError as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
